import json
import os # 파이썬을 이용해 시스테 내부 접근 가능

TASK_FILE = 'tasks.json'

def save_task(tasks): # 파일을 저장하는 기능
    with open(TASK_FILE, "w", encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii = False) # json 형식으로 파일 저장 indent는 파이썬 문법에 맞게 4칸으로 지정

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []
        

def show_menu():
    print("작업 관리 애플리케이션")
    print("1. 할일 목록")
    print("2. 할일 추가")
    print("3. 할일 완료")
    print("4. 할일 수정")
    print("5. 할일 삭제")
    print("6. 종료")

def view_task():
    pass


def add_task(task_name):
    tasks = load_tasks()
    tasks =[]
    task = {"name":task_name, "완료 여부": False}
    tasks.append(task)
    save_task(tasks)
    
def complete_task(task_no):
    pass

def fix_task(task_no, fix_task):
    pass
def delete_task(task_no):
    try:
        tasks = load_tasks()
        if 1<= task_no >= len(tasks):
            delete_tsk = tasks.pop(task_no -1)
            save_task(tasks)
            print(f"할 일: {delete_tsk['name']}이(가) 삭제되었습니다.")
        else:
            print("유효한 값을 입력해 주세요")
    except IndexError as e:
        print("리스트에 해당 항목이 없습니다.")

def main():
    while True:
        show_menu()
        choice = input("원하는 메뉴를 선택하세요".split(' '))
        if choice == "1" or choice =="할일목록":
            view_task()
        elif choice == "2" or choice =="할일추가":
            task =input("할 일을 추가해 주세요: ")
            add_task(task)
        elif choice == "3" or choice == "할일완료":
            task_num = int(input("완료 처리 할 번호를 입력해 주세요"))
            complete_task(task_num)
        elif choice == "4" or choice =="할일수정":
            task_num = int(input("수정할 번호를 입력해 주세요"))
            fix_task(task_num)
        elif choice == "5" or choice =="할일삭제":
            task_num = int(input("삭제할 번호를 입력해 주세요"))
            delete_task(task_num)
        elif choice == "6" or choice =="종료":
            print("System을 종료합니다.")
            break
        else:
            "유효하지 않은 값을 입력하였습니다. 다시 입력하세요"

task_list= {}

main()
