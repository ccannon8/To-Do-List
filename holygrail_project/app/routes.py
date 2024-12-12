from flask import Blueprint, render_template, jsonify, request, current_app

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    tasks = current_app.task_manager.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@bp.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = current_app.task_manager.get_all_tasks()
    return jsonify(tasks)

@bp.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    success = current_app.task_manager.add_task(
        data['task'],
        data['due_date'],
        int(data['priority'])
    )
    return jsonify({'success': success})

@bp.route('/api/tasks/<int:task_index>', methods=['PUT'])
def update_task(task_index):
    data = request.json
    if 'done' in data:
        success = current_app.task_manager.mark_done(task_index)
    else:
        success = current_app.task_manager.edit_task(
            task_index,
            data['task'],
            data['due_date'],
            int(data['priority'])
        )
    return jsonify({'success': success})

@bp.route('/api/tasks/<int:task_index>', methods=['DELETE'])
def delete_task(task_index):
    success = current_app.task_manager.delete_task(task_index)
    return jsonify({'success': success})