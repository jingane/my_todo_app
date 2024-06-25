import streamlit as st
import json
from pathlib import Path

# 데이터 파일 경로 설정
DATA_FILE = Path('data/todos.json')

# 데이터 파일 로드 함수
def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

# 데이터 파일 저장 함수
def save_data(todos):
    with open(DATA_FILE, 'w') as f:
        json.dump(todos, f)

# TODO 항목 추가 함수
def add_todo():
    todo_text = st.text_input('TODO 내용 입력:')
    stars = st.radio('중요도:', [1, 2, 3, 4, 5], index=4, format_func=lambda x: '★' * x)
    if st.button('추가'):
        if todo_text:
            todos.append({'text': todo_text, 'stars': stars})
            save_data(todos)
            st.experimental_rerun()

# TODO 항목 삭제 함수
def delete_todo():
    if todos:
        todo_index = st.selectbox('삭제할 TODO 선택:', range(len(todos)), format_func=lambda x: todos[x]['text'])
        if st.button('삭제'):
            todos.pop(todo_index)
            save_data(todos)
            st.experimental_rerun()

# TODO 데이터 로드
todos = load_data()

# TODO 항목 표시 함수
def display_todos():
    st.header('TODO 리스트')
    for idx, todo in enumerate(sorted(todos, key=lambda x: x['stars'], reverse=True)):
        st.write(f"{idx+1}. {todo['text']} (중요도: {'★' * todo['stars']})")

# Streamlit 앱 구조
st.title('TODO 관리 앱')
display_todos()
st.subheader('TODO 추가')
add_todo()
st.subheader('TODO 삭제')
delete_todo()
