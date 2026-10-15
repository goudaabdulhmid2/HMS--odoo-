# Hospital Management System (HMS) — Odoo Custom Module

A custom Odoo ERP module for managing patients, doctors, and hospital departments. This project demonstrates Odoo module development using Python, the Odoo ORM, XML views, access control, and QWeb reporting.

## Features

- **Patient Management:** Manage patient profiles, including names, email addresses, birth dates, medical history, blood types, addresses, images, and health status.
- **Data Validation:** Implement email format validation, duplicate patient email checks, and age validation.
- **Computed Fields:** Calculate patient age and expose related department information.
- **Relational Data Models:** Connect patients with doctors and departments using Odoo ORM relationships.
- **Patient Status Management:** Support patient health statuses such as Good, Fair, and Serious.
- **Odoo UI Customization:** Configure views for patients, doctors, and departments.
- **Contacts Integration:** Extend Odoo's `res.partner` model with patient-related functionality.
- **Access Control:** Configure model access permissions and record rules to restrict patient record access based on ownership.
- **QWeb Reporting:** Generate patient reports containing relevant patient and hospital information.

## Tech Stack

- **Language:** Python
- **ERP Framework:** Odoo
- **ORM:** Odoo ORM
- **Database:** PostgreSQL
- **UI & Configuration:** XML
- **Reporting:** QWeb
- **Version Control:** Git & GitHub

## Project Structure

```text
hms/
├── __manifest__.py
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── patient.py
│   ├── doctor.py
│   ├── department.py
│   └── res_partner.py
├── security/
│   ├── security.xml
│   ├── record_rules.xml
│   └── ir.model.access.csv
├── views/
└── reports/
    └── patient_report.xml
```

## Installation

This module requires an existing Odoo installation.

1. Clone the repository:

   ```bash
   git clone https://github.com/goudaabdulhmid2/HMS--odoo-.git
   ```

2. Copy the `hms` module directory into a directory included in your Odoo `addons_path`.
3. Restart the Odoo server.
4. Log in to Odoo and enable Developer Mode.
5. Navigate to **Apps**, update the Apps List, search for **HMS Module**, and install it.

If the module does not appear, verify that the addons directory is configured correctly and that the module files are accessible to the Odoo process.

## Data Models

| Model | Responsibility |
|---|---|
| `hms.patient` | Patient profiles, medical information, validation, and health status |
| `hms.doctors` | Doctor information |
| `hms.department` | Department details, capacity, and availability |
| `res.partner` | Integration between patient records and Odoo Contacts |

## Security

The module includes model-level access permissions and record rules for patient records. The configured patient record rule restricts access based on record ownership.

Security settings should be reviewed and tested before using the module with real patient data.

## Learning Outcomes

- Building custom modules in Odoo.
- Designing relational models using the Odoo ORM.
- Implementing computed fields, constraints, and validation logic.
- Customizing Odoo views and extending existing models.
- Configuring access rights and record rules.
- Creating QWeb reports.

## Project Status

This project is intended as a learning and demonstration project for Odoo ERP customization. It is not a production-ready hospital information system.

## Author

**Abdulhamid**

[GitHub Profile](https://github.com/goudaabdulhmid2)

## Repository

[View the project on GitHub](https://github.com/goudaabdulhmid2/HMS--odoo-)
