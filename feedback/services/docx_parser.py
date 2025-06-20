from docx import Document
import fitz

def extract_docx_comments(file_path):
    document = Document(file_path)
    comments_data = []

    # access comments stored in document part's comments.xml
    comments_part = document.part.package.part_related_by("http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments")
    
    if not comments_part:
        return []

    comments_xml = comments_part.blob
    from xml.etree import ElementTree as ET
    tree = ET.fromstring(comments_xml)

    for comment in tree.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}comment"):
        author = comment.attrib.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}author')
        text_elements = comment.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t")
        text = "".join(t.text for t in text_elements if t.text)

        comments_data.append({
            "author": author,
            "text": text,
            "position": "unknown",  # You can improve this based on paragraph markers
            "page": None  # Optional: Word doesn't store comment page numbers directly
        })

    return comments_data


def extract_pdf_comments(file_path):
    doc = fitz.open(file_path)
    comments_data = []

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        annotations = page.annots()

        if annotations:
            for annot in annotations:
                comment = annot.info.get("content", "")
                author = annot.info.get("title", "")
                rect = annot.rect

                # Heuristic: top/bottom/middle based on vertical position
                page_height = page.rect.height
                y_center = rect.y0 + rect.height / 2

                if y_center < page_height / 3:
                    position = "top"
                elif y_center > 2 * page_height / 3:
                    position = "bottom"
                else:
                    position = "middle"

                comments_data.append({
                    "author": author or "Unknown",
                    "text": comment.strip(),
                    "page": page_index + 1,
                    "position": position
                })

    return comments_data
