# Team Git Workflow (Zero-Conflict Guide)

To prevent merge conflicts while all 5 members work in parallel, follow these exact steps:

## 1. Strict Folder Rule
Only edit and commit files inside **your own named folder**:
- Randre Fearon -> `randre_fearon/`
- Amanda Morgan -> `amanda_morgan/`
- Ashaya Watts -> `ashaya_watts/`
- Tyrone Palmer -> `tyrone_palmer/`
- Shakir Russell -> `shakir_russell/`

> If you need a change in `shared/` or `resources/design/`, message the group chat first so everyone agrees before anyone edits it.

## 2. Create Your Own Branch
```bash
git pull origin main
git checkout -b member/<your-first-name>
# Example: git checkout -b member/randre
```

## 3. Commit & Push Only Your Folder
```bash
# Stage ONLY your folder
git add <your_folder_name>/

# Check what you are committing (make sure no other folder is listed!)
git status

# Commit with a clear message tied to your Feature ID
git commit -m "F-01: implement Bill of Lading search and delayed highlight"

# Push your branch
git push -u origin member/<your-first-name>
```

## 4. Integration / Fusion Day
Once every member's branch passes their folder's `pytest` tests:
1. Open a Pull Request into `main`.
2. Merge each member's PR one by one (zero conflicts since folders are completely isolated).
3. Run `pytest` across all folders + `integration/test_end_to_end.py`.
4. Verify the fused app runs smoothly via `python app.py` and deploy to Vercel.
