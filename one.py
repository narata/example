class Stack():
    def __init__(st,size):
        st.stack = []
        st.size = size
        st.top = -1

    def push(st,content):
        if st.full():
            print("Stack is Full !")
        else:
            st.stack.append(content)
            st.top = st.top + 1

    def full(st):
        if st.top == st.size:
            return True
        else:
            return False

    def empty(st):
        if st.top == -1:
            print("Stack is Empty")
    