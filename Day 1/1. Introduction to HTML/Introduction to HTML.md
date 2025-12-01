## 1. What is HTML?

- **HTML = Hyper Text Markup Language**
- Not a programming language → **markup language**
- Type of **SGML** (Standard Generalized Markup Language)
- Uses **markup tags** to describe webpages
- HTML file = text file containing markup tags  
    Example: `<p>`
- File extensions: `.html` or `.htm`
---
## 2. Markup Languages

- Markup = embedded **codes (tags)** in documents
- Tags:
    - Describe structure
    - Provide instructions for processing/rendering
- Markup language = defines syntax for tags
---
## 3. HTML Elements
- Tags are enclosed in `< >`
- Usually come in pairs:
    - `<p>` opening tag
    - `</p>` closing tag
- Content between tags = **element content**
- Tags are **not case-sensitive** (but lowercase is standard)
---
## 4. Advantages of HTML
- Easy to learn and use
- Loose syntax
- Supported by all browsers
- Ubiquitous across the web
- Similar to XML
- Free
- Beginner-friendly
## 5. Disadvantages of HTML

- Not dynamic by itself (requires JS/PHP etc.)
- Structuring complex docs can be difficult
- Must avoid deprecated tags
- Limited security features
---
## 6. Structural Tags

| Tag                  | Purpose                              |
| -------------------- | ------------------------------------ |
| `<html>...</html>`   | Entire webpage                       |
| `<head>...</head>`   | Metadata section                     |
| `<title>...</title>` | Title shown in browser tab/bookmarks |
| `<body>...</body>`   | Visible content                      |

### Sample HTML Structure
``` HTML
<html>
  <head>
    <title>John Q. Public's Web Page</title>
  </head>
  <body>
    This is John Public's Webpage!
  </body>
</html>
```
---
## 7. Header Tags

- `<h1>` → largest
- `<h6>` → smallest  
    All headers are bold by default.

---
## 8. Paragraphs & Line Breaks

- Paragraph:  
    `<p>text</p>`
- Line break:  
    `<br>`

---
## 9. Horizontal Rule `<hr>`
Attributes:
- `NOSHADE`
- `WIDTH="xx%"` or pixel value
- `SIZE="x"` → height
- `ALIGN="left|center|right"`
---
## 10. Text Formatting Tags

| Tag         | Effect            |
| ----------- | ----------------- |
| `<i>`       | Italic            |
| `<b>`       | Bold              |
| `<pre>`     | Preformatted text |
| `<strong>`  | Strong emphasis   |
| `<address>` | Address           |
| `<cite>`    | Citation          |
| `<code>`    | Code text         |

---
## 11. Font Modifications (`<font>` — deprecated in HTML5)
Attributes:
- `size="1-7"`
- `color="red"`
- `face="verdana"`

---
## 12. Lists
### Unordered List
``` HTML
`<ul>   <li>Item</li> </ul>`
```

Types:
- `disc` (default)
- `circle`
- `square`
### Ordered List
``` HTML
`<ol type="a" start="3">...</ol>`
```

Types:
- `1`, `a`, `A`, `i`, `I`

### Definition List
``` HTML
<dl>
  <dt>Term</dt>
  <dd>Description</dd>
</dl>
```
---

## 13. Links (`<a>`)

- Basic link:  
    `<a href="url">text</a>`
- Internal anchor:  
    `<a href="#section">Jump</a>`
- Email link:  
    `<a href="mailto:someone@mail.com">Email</a>`

---
## 14. Graphics (`<img>`)

Attributes:

- `src="image_path"`
- `alt="description"`
- `width=""`, `height=""`
- `border=""`
- `hspace=""`, `vspace=""`
- `align="top|middle|bottom|left|right"`

---
## 15. Marquee Tag (deprecated)
``` HTML
`<marquee>text</marquee>`
```

Attributes:

- `bgcolor`
- `direction`
- `width`
- `loop`

## **Assignment**

Create your résumé as a webpage.