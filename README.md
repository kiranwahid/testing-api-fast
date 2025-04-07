
## 📚 API Endpoints and How to Use

### 1. 📥 GET Request

- **URL:** `http://127.0.0.1:8000/`
- **Use:** Get the list of all names.
- **How:**
  - Open your browser and visit 👉 `http://127.0.0.1:8000/`
  - Or use **Postman** / **cURL**:
    ```bash
    curl http://127.0.0.1:8000/
    ```

---

### 2. ➕ POST Request

- **URL:** `http://127.0.0.1:8000/data`
- **Use:** Add a new name to the list.
- **Send JSON body:**
  ```json
  {
    "name": "new_name"
  }
  ```
- **How:**
  - In Postman, select **POST**, put the URL, and under **Body > raw > JSON**, send:
    ```json
    {
      "name": "John"
    }
    ```
  - Or using cURL:
    ```bash
    curl -X POST "http://127.0.0.1:8000/data" -H "Content-Type: application/json" -d "{\"name\":\"John\"}"
    ```

---

### 3. 🗑 DELETE Request

- **URL:** `http://127.0.0.1:8000/{name}`
- **Use:** Delete a name from the list.
- **Example:**  
  To delete **"kiran"**, send a DELETE request to:  
  `http://127.0.0.1:8000/kiran`
- **How:**
  - In Postman, select **DELETE**, and put the full URL with the name you want to remove.

---

### 4. ♻️ PUT Request

- **URL:** `http://127.0.0.1:8000/{name}`
- **Use:** Update an existing name in the list.
- **Send JSON body:**
  ```json
  {
    "name": "new_name"
  }
  ```
- **Example:**  
  To update **"muskan"** to **"ayesha"**, send a PUT request to:  
  `http://127.0.0.1:8000/muskan`
- **How:**
  - In Postman, select **PUT**, enter the URL, and in **Body > raw > JSON**, send:
    ```json
    {
      "name": "ayesha"
    }
    ```
  - Or using cURL:
    ```bash
    curl -X PUT "http://127.0.0.1:8000/muskan" -H "Content-Type: application/json" -d "{\"name\":\"ayesha\"}"
    ```

---

## 🌟 That's it!

Enjoy using your FastAPI project! 🎉  
You can also check the automatic API docs here:  
- Swagger UI 👉 `http://127.0.0.1:8000/docs`

---
