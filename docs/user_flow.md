# User Flow Guide

## Overview
The app processes requests through a clear flow from API routes to services to models.

## Step-by-Step Flow
1. **User Interaction**
   - User sends a request to an API endpoint:
     - `/analysis` → `analysis_routes.py`
     - `/evaluation` → `evaluation_routes.py`
     - `/recommendation` → `recommendation_routes.py`
2. **Routes**
   - Routes receive requests and call the corresponding service.
3. **Services**
   - Services process data, load ML models, and perform analysis.
   - Example: `analysis_service.py` → calls `decision_tree_model.py`
4. **Data Handling**
   - JSON resources (`questions.json`, `resources.json`) are loaded using `data_loader.py`
5. **Response**
   - Processed data is returned as JSON to the user.
6. **Testing**
   - All flows are covered in `tests/test_routes.py` and `tests/test_services.py`
