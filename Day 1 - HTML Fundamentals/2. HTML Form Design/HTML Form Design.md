## 1. What Are Forms?

- Used to **collect user input**
- Wrapped inside `<form>...</form>`
- Form contains multiple input elements
- After filling, user clicks **Submit**

---
## 2. Common Form Fields

- Text boxes
- Password boxes
- Checkboxes
- Radio buttons
- Submit / Reset buttons
- Dropdown lists (`<select>`)
- Textareas
- Labels
- Fieldsets & Legends

---
## 3. Form Attributes

### **1. `action`**

Defines where form data is sent.
``` HTML
<form action="/action_page.php">
```
### **2. `method`**

- `GET`
    - Default
    - Data visible in URL
    - Limited length
    - Not secure
    - Bookmarkable results
- `POST`
    - Data hidden from URL
    - No size limit
    - Secure data
```HTML
<form method="post">
```
### **3. `autocomplete`**
``` HTML
<form autocomplete="on">
```
### **4. `novalidate`**
Skips browser validation.
### **5. `name`**
Identifies the form.

---
## 4. `<input>` Element

Main element for user input.

Attributes:

- `type`
- `name` _(required for submission)_
- `value`
- `size`
- `maxlength`
- `readonly`
- `disabled`
---
## 5. Types of `<input>`

### **Text Box**
``` HTML
<input type="text">
```
### **Password Box**
```HTM
<input type="text">
```
`<input type="password">`

### **Radio Button**

- Only **one selected** per group
- Same `name`, different `value`
``` HTML
<input type="radio" name="gender" value="male" checked>
```
### **Checkbox**
- Allows **multiple selections**
``` HTML
<input type="checkbox" name="skill" value="html">
```
### **Submit Button**
``` HTML
<input type="submit" value="Send">
```

### **Reset Button**
``` HTML
<input type="reset" value="Clear">
```

---
## 6. `<textarea>`

``` HTML
<textarea rows="5" cols="40"></textarea>
```

Used for multi-line input.

---

## 7. `<select>` and `<option>`
``` HTML
<select name="dept" size="3" multiple>
  <option value="cse" selected>CSE</option>
</select>
```

Attributes:

- `size`
- `multiple`
- `selected`

---

## 8. `<label>`

Improves accessibility.
``` HTML
<label for="email">Email</label>
<input id="email" type="text">
```

---
## 9. `<button>`

Supports richer content compared to `<input type="button">`
``` HTML
<button type="submit">
  <img src="icon.png"> Submit
</button>
```

---
## 10. `<fieldset>` and `<legend>`

Group related form items.
``` HTML
<fieldset>
  <legend>Personal Info</legend>
  ...
</fieldset>
```

---

## 11. HTML5 New Input Types

- `range`
- `search`
- `tel`
- `time`
- `url`
- `week`
- `color`
- `date`
- `datetime-local`
- `email`
- `month`
- `number`

Unsupported browsers treat them as `text`.

---
## **Assignment**

Create a _Campus Placement Registration Form_ using HTML.