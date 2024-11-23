
---

# **GenAI Python Developer Helper**

### 🚀 **Description**
This application leverages the power of **Google's Generative AI** to assist Python developers by generating meaningful responses to their queries. Designed with simplicity and productivity in mind, the app comes with an interactive user interface built using **Streamlit**.

---

## **🌟 Features**
- **Generate Python Development Help**:
  - Get concise, AI-powered responses to Python-related queries.
- **Log Queries and Responses**:
  - Saves unique queries and responses to a log file (`data_log.txt`) for easy retrieval.
- **View Logs**:
  - Displays previously saved queries and their responses.
- **Validation & Error Handling**:
  - Ensures only meaningful and unique inputs are processed.
- **User-Friendly Interface**:
  - Interactive GUI with a sidebar menu for easy navigation.
  
---

## **🛠️ Technologies Used**
- **Python**: Core programming language.
- **Streamlit**: For building an interactive GUI.
- **Google Gemini Generative AI**: For generating responses to user queries.
- **File Handling**: Logs stored in external files for persistence.

---
## **📋 Requirements**
To run the project, ensure you have the following installed:
- **Python 3.8+**

---

## **💻 How to Run the App**
1. Clone this repository:
   ```bash
   git clone https://github.com/akdenizler/genai-python-helper.git
   cd genai-python-helper
   ```

2. **Run the following commands**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -q -U google-generativeai
   pip install streamlit
   export GENAI_API_KEY="YOUR_KEY_FROM_GOOGLE_GEMINI"
   ```
   
3. Run the application:
   ```bash
   

   streamlit run main.py
   ```

4. Open your browser at [http://localhost:8501](http://localhost:8501) to use the app.

---

## **🗂️ App Features in Detail**

### **1. Generate Responses**
- **How It Works**:
  - Enter your query into the text box.
  - Press the "Generate" button.
  - WAIT(THATS IMPORTANT IT TAKES TIME)
  - The AI generates a response that is displayed in a text area.
  - Unique queries are logged along with their responses.

### **2. View Log**
- **Purpose**:
  - Displays all previously processed queries and their responses.
  - Useful for reviewing past interactions without re-running queries.

### **3. About Section**
- **Details**:
  - Provides an overview of the app and its features.

---

## **📊 Functional Requirements Checklist**

| Requirement                             | Status | Notes                                                                                     |
|-----------------------------------------|--------|-------------------------------------------------------------------------------------------|
| **Solves a meaningful problem**         | ✅     | Helps Python developers with coding-related queries.                                      |
| **User interaction menu**               | ✅     | Sidebar with three sections: "Generate Response," "View Log," and "About."               |
| **Deployed on Git**                     | ✅     | Code is modular and Git-friendly.                                                        |
| **README.md**     | ✅     | Fully detailed README.md                                    |
| **Uses external file to save data**     | ✅     | Logs queries and responses to `data_log.txt`.                                            |
| **Display and save data**               | ✅     | Queries and responses are saved and displayed on-demand.                                 |
| **Uses API**                            | ✅     | Integrates with Google Generative AI.                                                    |
| **Uses dicts, lists, sets, tuples**     | ✅     | Uses **set** for unique prompts and **list of tuples** for in-memory query-response pairs.|
| **Exception handling and validation**   | ✅     | Validates inputs and handles API/file-related errors gracefully.                         |
| **No code outside functions**           | ✅     | All reusable logic is modularized into `ai_utils.py` and `file_utils.py`.                |
| **Under 150 lines per file**            | ✅     | The code is modular, with functions in separate files for readability and organization.   |

---

## **✨ Future Enhancements**
- **Authentication**:
  - Add user authentication for personalized logs.
- **Advanced AI Features**:
  - Allow users to select different AI models or modes.
- **Cloud Integration**:
  - Sync logs to cloud storage (e.g., Google Drive or AWS S3).

---

## **📜 License**
This project is licensed under the same license as Google Gemini. Feel free to use, modify, and distribute this application as needed.

---

## **📧 Contact**
**Developer**: Deniza Suleymanova  
**Email**: [kyzyldeniz@gmail.com]  
**GitHub**: [https://github.com/akdenizler](https://github.com/akdenizler)

---