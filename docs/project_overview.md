# Project Overview: Hackathon Sofrecom Diagnostic Raida

## Project Name
Hackathon Sofrecom Diagnostic Raida

## Description
This project is a web-based backend system built using Python and Flask, designed to provide automated data analysis, evaluation, and recommendation services. It leverages machine learning models for predictive insights and aims to streamline decision-making for diagnostic processes.

## Goals
- Provide a centralized backend for data ingestion, processing, and analytics.
- Deliver accurate recommendations based on predictive models.
- Ensure scalable and modular architecture for future expansion.

## Technology Stack
- **Backend Framework**: Flask 3.0
- **Programming Language**: Python 3.12
- **Libraries & Tools**:
  - Pandas, NumPy for data processing
  - Scikit-learn for ML modeling
  - Joblib for model persistence
- **Environment**:
  - Virtual Environment (venv)
  - RESTful API endpoints

## Key Components
1. **app/main.py** – Initializes the Flask application.
2. **app/routes/** – Contains API route definitions:
   - `analysis_routes.py`
   - `evaluation_routes.py`
   - `recommendation_routes.py`
3. **app/services/** – Business logic and ML services:
   - `analysis_service.py`
   - `evaluation_service.py`
   - `recommendation_service.py`
4. **run.py** – Entry point for launching the application.

## Target Audience
- Internal diagnostic teams
- Data analysts requiring predictive insights
- AI agents that may interface with this backend

## Status
- Development in progress
- ML models being integrated and tested
