Added JSON Validator Bot, Error Reports & Cleaned Contributor Data (Fixes #330)


Hi @amyyalex (Repo Owner),  

We (me @kronpatel and my brother @jeturgavli) worked on **Issue #330** and implemented a **JSON Validator Bot** to ensure all contributor data in `cardDetails.json` stays valid and clean.  

### 🔹 What’s Added / Changed
- **`validator.py` Script**  
  - Checks for required fields: `name`, `profession`, `quote`, `github`  
  - Detects duplicate entries (Name + GitHub link)  
  - Validates emails → must start with `mailto:`  
  - Warns if optional fields (`twitter`, `linkedin`, `behance`, `dribbble`) still use default values  
  - Detects duplicate links across optional fields  

- **GitHub Workflow Action**  
  - Runs validation automatically on every PR affecting `cardDetails.json`  
  - Prevents invalid contributions from being merged  

- **Reports System (`/reports/`)** *(manually created for demonstration)*  
  - `normal_report.txt` → Detailed validation logs  
  - `with_name_report.txt` → Errors grouped with contributor names  
  - `Email_Valid_Report.txt` → Email-specific validation issues  
  - `default_links_and_dublicate_links_report.txt` → Default/duplicate link checks  
  - ⚠️ **Note:** These report files were created manually just to demonstrate how error reporting can look.  
    You may **clear or delete the `/reports/` folder** if not required in the repository. 

- **Cleaned `cardDetails.json`**  
  - Removed all invalid / duplicate / placeholder entries  
  - Ensures future contributions remain bot-guided and error-free  

---

## 🎯 Impact
- Maintains high project quality by blocking invalid JSON entries.  
- Reduces manual review work for maintainers.  
- Improves contributor experience with clear, automated error reports.  

---

## 🙌 Bot Contributor
- @kronpatel  
- @jeturgavli  

## 🔗 Linked Issue
Fixes #330  
