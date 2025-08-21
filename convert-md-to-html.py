#!/usr/bin/env python3
import re

def convert_md_to_html(md_file, html_file, title="Terms & Conditions"):
    """Convert Markdown to HTML with custom styling"""
    
    with open(md_file, 'r') as f:
        content = f.read()
    
    # HTML template
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - TaxSnap</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #4CAF50;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 15px;
            margin-bottom: 30px;
        }}
        h2 {{
            color: #388E3C;
            margin-top: 30px;
            margin-bottom: 15px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
        }}
        h3 {{
            color: #555;
            margin-top: 20px;
        }}
        .header-info {{
            background: #f8f8f8;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 30px;
        }}
        .header-info strong {{
            color: #4CAF50;
        }}
        ul, ol {{
            padding-left: 30px;
        }}
        li {{
            margin: 8px 0;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
        }}
        strong {{
            color: #2E7D32;
        }}
        .back-to-top {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #4CAF50;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            text-decoration: none;
            display: none;
        }}
        .back-to-top:hover {{
            background: #45a049;
        }}
        .footer {{
            margin-top: 50px;
            padding-top: 20px;
            border-top: 2px solid #4CAF50;
            text-align: center;
            color: #666;
        }}
        @media (max-width: 600px) {{
            .container {{
                padding: 20px;
            }}
            body {{
                padding: 10px;
            }}
        }}
        @media print {{
            .back-to-top {{
                display: none !important;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {content}
        <div class="footer">
            <p><a href="index.html">← Back to Legal Documents</a></p>
            <p>&copy; 2024 DIMLAR Consulting Pty Ltd. All rights reserved.</p>
        </div>
    </div>
    <a href="#" class="back-to-top" id="backToTop">↑ Top</a>
    <script>
        // Show/hide back to top button
        window.onscroll = function() {{
            var button = document.getElementById('backToTop');
            if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {{
                button.style.display = "block";
            }} else {{
                button.style.display = "none";
            }}
        }};
    </script>
</body>
</html>"""
    
    # Convert markdown to HTML
    html_content = content
    
    # Convert headers
    html_content = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
    
    # Convert bold
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_content)
    
    # Convert italic
    html_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_content)
    
    # Convert line breaks
    html_content = re.sub(r'^---$', r'<hr>', html_content, flags=re.MULTILINE)
    
    # Convert lists
    html_content = re.sub(r'^- (.*?)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    
    # Wrap consecutive li elements in ul
    html_content = re.sub(r'(<li>.*?</li>\n)+', lambda m: '<ul>\n' + m.group(0) + '</ul>\n', html_content)
    
    # Convert paragraphs
    lines = html_content.split('\n')
    formatted_lines = []
    in_list = False
    
    for line in lines:
        line = line.strip()
        if line:
            if line.startswith('<h') or line.startswith('<ul') or line.startswith('</ul'):
                formatted_lines.append(line)
            elif line.startswith('<li'):
                if not in_list:
                    formatted_lines.append('<ul>')
                    in_list = True
                formatted_lines.append('  ' + line)
            else:
                if in_list:
                    formatted_lines.append('</ul>')
                    in_list = False
                if not line.startswith('<'):
                    formatted_lines.append(f'<p>{line}</p>')
                else:
                    formatted_lines.append(line)
    
    if in_list:
        formatted_lines.append('</ul>')
    
    html_content = '\n'.join(formatted_lines)
    
    # Create full HTML
    final_html = html_template.format(title=title, content=html_content)
    
    # Write to file
    with open(html_file, 'w') as f:
        f.write(final_html)
    
    print(f"Converted {md_file} to {html_file}")

if __name__ == "__main__":
    # Convert Terms & Conditions
    convert_md_to_html(
        "/home/vxl1/MyApps/tax-snap-app/tax_snap/docs/terms-and-conditions.md",
        "/home/vxl1/MyApps/tax-snap-app/tax_snap/docs/terms-v2.html",
        "Terms & Conditions v2.0"
    )
    
    # Convert Privacy Policy
    convert_md_to_html(
        "/home/vxl1/MyApps/tax-snap-app/tax_snap/docs/privacy-policy.md",
        "/home/vxl1/MyApps/tax-snap-app/tax_snap/docs/privacy-v1.html",
        "Privacy Policy v1.0"
    )