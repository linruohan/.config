const form = document.getElementById('task-form');
const taskInput = document.getElementById('task');
const filterInput = document.getElementById('filter');
// const removebtn = document.querySelector('.delete-item');
const clearbtn = document.querySelector('.clear-tasks');
//所有任务列表
const taskUl = document.querySelector('.collection');


//存储数据
let tasks = ['任务 1', '任务 2'];

//0. 启动
startApp();

function startApp() {

    //显示tasks
    showTasks(tasks);
    //开始监听
    startListen();

}

function showTasks(tasks) {
    taskUl.innerHTML = '';

    for (const task of tasks) {
        //生成
        let li = document.createElement('Li');
        li.className = 'collection-item';
        li.innerHTML = `${task} <a class="delete-item secondary-content"><i class="fa fa-remove"></i></a>`;
        //插入到最前面
        taskUl.append(li);
    }
}


function startListen() {

    // add 添加
    form.addEventListener('submit', addTask);
    // remove 单个任务
    taskUl.addEventListener('click', removeTask);
    // 删除所有任务
    clearbtn.addEventListener('click', clearAllTasks);
    // 筛选任务
    filterInput.addEventListener('keyup', filterTasks);


}


function addTask(e) {
    //输入内容
    const newTask = taskInput.value;
    tasks.unshift(newTask);
    showTasks(tasks);
    taskInput.value = '';
    //防止刷新
    e.preventDefault();
}

function removeTask(e) {
    if (e.target.classList.contains('fa-remove')) {
        // e.target.parentNode.parentNode.remove();
        let index = tasks.indexOf(e.target.parentNode.parentNode.firstChild.textContent);
        tasks.splice(index, 1);
        showTasks(tasks);
    }
}

function clearAllTasks() {
    // console.log(taskUl);
    // taskUl.innerHTML = '';
    tasks = [];
    showTasks(tasks);
}

function filterTasks(e) {
    const inputText = e.target.value.toLowerCase(); //.toLowerCase()忽略大小写
    // document.querySelectorAll('.collection-item').forEach(function(taskLi) {
    //     const item = taskLi.firstChild.textContent.toLowerCase();
    //     if (item.indexOf(inputText) != -1) {
    //         // 包含
    //         taskLi.style.display = 'block'; //显示
    //         taskLi.classList.remove('hide');
    //     } else {
    //         // 不包含
    //         taskLi.style.display = 'none'; //隐藏
    //         taskLi.classList.add('hide');

    //     }
    // })
    const filterTasks = tasks.filter(task => task.toLowerCase().includes(inputText));
    showTasks(filterTasks);

}