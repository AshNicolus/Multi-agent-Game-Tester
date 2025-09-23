from fastapi import FastAPI
from pydantic import BaseModel
import asyncio 
import json
import playwright.async_api import async_playwright
from typing import List
import os 




class TestStep(BaseModel):
    action: str
    target:str
    value:str = ""
class TestCase(BaseModel):
    name:str
    steps:List[TestStep]
class TestReport(BaseModel):
    test_case:str
    verdict:str
    artificts:List[str]
    reproducibility: int
    notes: str


class PlannerAgent:
    """Generate Candidate Test Cases"""
    def generate_test_cases(self) -> List[TestCase]:
        tests = []
        for i in range(20):
            tests.append(TestCase(
                name=f"Test Case {i+1}",
                steps = []
            ))
app = FastAPI()
