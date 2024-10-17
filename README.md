# Ramani Chabot Backend

## Overview

## APis

### Summary of Endpoints

| Endpoint              | HTTP Method | Purpose                                       |
| --------------------- | ----------- | --------------------------------------------- |
| `/employers/`         | GET/POST    | List or create employers                      |
| `/employers/<id>/`    | GET/PUT/DEL | Retrieve, update, or delete an employer       |
| `/employees/`         | GET/POST    | List or create employees                      |
| `/employees/<id>/`    | GET/PUT/DEL | Retrieve, update, or delete an employee       |
| `/jobs/`              | GET/POST    | List or create job listings                   |
| `/jobs/<id>/`         | GET/PUT/DEL | Retrieve, update, or delete a job listing     |
| `/applications/`      | GET/POST    | List or create job applications               |
| `/applications/<id>/` | GET/PUT/DEL | Retrieve, update, or delete a job application |
| `/hirings/`           | GET/POST    | List or create hirings                        |
| `/hirings/<id>/`      | GET/PUT/DEL | Retrieve, update, or delete a hiring record   |
| `/api/token/`         | POST        | Obtain JWT token                              |
| `/api/token/refresh/` | POST        | Refresh JWT token                             |

#### **Filtering via URL (Optional)**

Users can filter the data directly from the browser with query parameters. For example:

- `/jobs/?title=Developer&job_type=full-time`: Returns jobs filtered by title and job type.
