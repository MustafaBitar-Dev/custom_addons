# Grades Module

## Grade Model Fields

### Main Field
- **Number** (`Integer`)
  - A unique integer
  - Greater than 0

### Specify Limits Fields
- **Disability Rate** (`Float`)
  - Value between **0 - 100**
- **Female Rate** (`Float`)
  - Value between **0 - 100**
- **Max Benefit** (`Float`)
  - Must be a positive number
- **Ability To Retire** (`Boolean`)

### Allowances Fields
(All fields must be a **positive number**)
- **Education** (`Float`)
- **Transport** (`Float`)
- **Medical** (`Float`)
- **Mobile** (`Float`)
- **Housing** (`Float`)

### Country Rates
(All fields must be a **number between 0 - 100**)
- **Egypt Rate** (`Float`)
- **Qatar Rate** (`Float`)
- **Other Country Rate** (`Float`)

## Grade Model Permissions
For now, **all users** have permission to:
- Create
- Read
- Update
- Delete

However, the permissions will later be restricted to the **`group_erp_manager`** user group.

