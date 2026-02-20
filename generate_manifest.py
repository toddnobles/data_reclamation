import os
import json

def generate_manifest():
    pdf_dir = 'examples'
    md_dir = 'test_batch_workspace/markdown'
    
    pdfs = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    mds = [f for f in os.listdir(md_dir) if f.endswith('.md')]
    
    pdf_map = {os.path.splitext(f)[0]: f for f in pdfs}
    
    manifest = []
    
    for md_file in mds:
        md_base = os.path.splitext(md_file)[0]
        # Check if there is a matching PDF
        if md_base in pdf_map:
            manifest.append({
                'name': md_base,
                'pdf': os.path.join(pdf_dir, pdf_map[md_base]),
                'md': os.path.join(md_dir, md_file)
            })
        elif md_base.endswith('_shrunk_pdf') and md_base[:-len('_shrunk_pdf')] in pdf_map:
             # Handle cases where md might have extra suffix but pdf doesn't (though looking at the list they seem to match well)
             pass
             
    # Sort manifest by name
    manifest.sort(key=lambda x: x['name'])
    
    with open('manifest.json', 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"Generated manifest.json with {len(manifest)} pairs.")

if __name__ == '__main__':
    generate_manifest()
