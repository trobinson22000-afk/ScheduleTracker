import csv
import json
import os

try:
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Path to the production CSV files
    production_csv = os.path.join(script_dir, 'jobList.csv')
    finishing_csv = os.path.join(script_dir, 'finishingList.csv')
    print("Script dir:", script_dir)
    print("Files in dir:", os.listdir(script_dir))
    # Read and parse the production CSV
    production_jobs = []
    if os.path.exists(production_csv):
        with open(production_csv, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('jobNumber') or row.get('itemNumber'):
                    job = {
                        'jobNumber': row.get('jobNumber', ''),
                        'itemNumber': row.get('itemNumber', ''),
                        'dieNumber': row.get('dieNumber', ''),
                        'material': row.get('material', ''),
                        'width': row.get('width', ''),
                        'footage': float(row.get('footage', 0)),
                        'dueDate': row.get('dueDate', ''),
                        'status': row.get('status', '').lower()
                    }
                    production_jobs.append(job)

    

    # Read and parse the finishing CSV
    finishing_jobs = []
    if os.path.exists(finishing_csv):
        with open(finishing_csv, 'r') as f:
            reader = csv.DictReader(f)
            print("Finishing headers:", reader.fieldnames)
            for row in reader:
                print("Row:", row)
                break
            for row in reader:
                if row.get('jobNumber') or row.get('itemNumber'):
                    job = {
                        'jobNumber': row.get('jobNumber', ''),
                        'itemNumber': row.get('itemNumber', ''),
                        'dieNumber': row.get('dieNumber', ''),
                        'material': row.get('material', ''),
                        'width': row.get('width', ''),
                        'footage': float(row.get('footage', 0)),
                        'dueDate': row.get('dueDate', ''),
                        'status': row.get('status', '').lower()
                    }
                    finishing_jobs.append(job)

    # Path to material inventory CSV
    material_csv = os.path.join(script_dir, 'material_inventory.csv')

    # Read and parse the material CSV
    materials = []
    if os.path.exists(material_csv):
        with open(material_csv, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                mat = {
                    'material': row.get('material', ''),
                    'width': row.get('width', ''),
                    'footage': float(row.get('footage', 0))
                }
                materials.append(mat)

        print("Materials loaded:", materials)

    # Convert to JSON strings
    production_jobs_json = json.dumps(production_jobs, ensure_ascii=True, indent=2)
    finishing_jobs_json = json.dumps(finishing_jobs, ensure_ascii=True, indent=2)
    materials_json = json.dumps(materials, ensure_ascii=True, indent=2)

    # Read the template HTML
    output_file = os.path.join(script_dir, 'panel.html')

    # Try to find panel_template
    template_file = os.path.join(script_dir, 'panel_template.html')

    if os.path.exists(template_file):
        with open(template_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Replace the placeholders with the actual data
        html_content = html_content.replace('let productionJobs = [];', f'let productionJobs = {production_jobs_json};')
        html_content = html_content.replace('let finishingJobs = [];', f'let finishingJobs = {finishing_jobs_json};')
        html_content = html_content.replace('let allMaterials = [];', f'let allMaterials = {materials_json};')

        # Write the output
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"Generated {output_file} with embedded job and material data.")
        print("SUCCESS!")
    else:
        print(f"\nERROR: Template file not found at {template_file}")
        print(f"Please verify the file exists and the name is exactly 'panel_template'")

except Exception as e:
    print(f"\nERROR: An exception occurred!")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {str(e)}")
    import traceback
    print("\nFull error details:")
    traceback.print_exc()

# Keep window open on Windows
input("\nPress Enter to close this window...")
