# mcp_server_q360.py
import os
import asyncio
import json
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.chains import RetrievalQA
import databases
import redis.asyncio as redis
import smtplib
from email.message import EmailMessage
from contextlib import asynccontextmanager
from sqlalchemy import create_engine, text

# ENV and Config
DATABASE_URL = "mssql+pyodbc://username:password@localhost/dbname?driver=ODBC+Driver+17+for+SQL+Server"

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = 587
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL", "support@example.com")

# Clients
engine = create_engine(DATABASE_URL)
redis_client = redis.from_url(REDIS_URL)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auth and tenant (simplified)
async def get_user_context(request: Request):
    token = request.headers.get("Authorization")
    # Simulate token decoding
    return {"user_id": "u1", "tenant_id": "t1"}

# Models
class Query(BaseModel):
    question: str

class ReportRequest(BaseModel):
    fields: list[str]
    filters: dict

class EmailRequest(BaseModel):
    subject: str
    message: str

class Message(BaseModel):
    to: str
    message: str

# LangChain RAG
CHROMA_PATH = "chroma_index"
DOCS_PATH = "./agile_docs/"

def answer_question_from_documents(question: str) -> str:
    vectordb = Chroma(persist_directory=CHROMA_PATH, embedding_function=OpenAIEmbeddings())
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=retriever
)
    return qa_chain.run(question)








from sqlalchemy.sql import text

@app.get("/api/ask_inspection_data")
def ask_inspection_data():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT TOP 10 * FROM inspections"))
        rows = [dict(row._mapping) for row in result]
    return {"data": rows}

@app.post("/api/ask_inspection_plans")
async def ask_inspection_plans(query: Query, ctx=Depends(get_user_context)):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT TOP 5 * FROM inspection_plans WHERE tenant_id = '{ctx['tenant_id']}'"))
        rows = [dict(row._mapping) for row in result]
    return {"data": rows}

@app.post("/api/ask_supplier_applications")
async def ask_supplier_applications(query: Query, ctx=Depends(get_user_context)):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT TOP 5 * FROM supplier_applications WHERE tenant_id = '{ctx['tenant_id']}'"));
        rows = [dict(row._mapping) for row in result];
    return {"data": rows};

@app.post("/api/ask_agile_docs")
async def ask_agile_docs(query: Query):
    answer = answer_question_from_documents(query.question)
    return {"answer": answer};          

@app.post("/api/generate_report")
async def generate_report(req: ReportRequest, ctx=Depends(get_user_context)):
    fields = ", ".join(req.fields)
    where_clauses = [f"{k} = '{v}'" for k, v in req.filters.items()]
    where_sql = " AND ".join(where_clauses)
    q = f"SELECT {fields} FROM inspections WHERE {where_sql} AND tenant_id = '{ctx['tenant_id']}'"
    with engine.connect() as conn:
        result = conn.execute(text(q))
        rows = [dict(row._mapping) for row in result]
    return {"report": rows}

@app.post("/api/send_ticket")
async def send_ticket(email: EmailRequest, ctx=Depends(get_user_context)):
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = SUPPORT_EMAIL
    msg["Subject"] = f"Support Request from {ctx['user_id']}: {email.subject}"
    msg.set_content(email.message)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
    return {"status": "ticket sent"}

@app.post("/api/send_message")
async def send_message(msg: Message, ctx=Depends(get_user_context)):
    redis_client.rpush(f"chat:{msg.to}", json.dumps({"from": ctx["user_id"], "msg": msg.message}))
    return {"status": "message sent"}



@app.get("/api/get_messages")
async def get_messages(ctx=Depends(get_user_context)):
    key = f"chat:{ctx['user_id']}"
    messages = await redis_client.execute_command("LRANGE", key, 0, -1)
    return {"messages": [json.loads(m) for m in messages]} if messages else []
