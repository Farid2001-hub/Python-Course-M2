# Advanced CLI Task Manager

## Features
- Add, list, delete tasks
- Subcommands with argparse
- Logging of all operations
- Environment variable support (`TASKS_FILE_PATH`)
- Unit tested core logic

## Usage

### Add Task
```bash
python3 -m task_manager.cli add "Finish project" --priority 2
```
### List Tasks
```bash
python3 -m task_manager.cli list
```
### Delete Task
```bash
python3 -m task_manager.cli delete 1
```
### Testing
```bash
python3 -m task_manager.cli delete 1



---

# 🚀 Résultat :
- Tu peux **ajouter, voir, supprimer** des tâches via des **subcommands**.
- Les actions sont **loggées** proprement dans `logs/task_manager.log`.
- Tu peux changer facilement le fichier JSON avec `TASKS_FILE_PATH`.
- Le code est **testé automatiquement** avec `unittest`.

---

Veux-tu aussi que je te prépare :
- Une **version installable** en mode `pip install .` (avec `setup.py`) ?
- Un **Makefile** pour lancer facilement (`make run`, `make test`) ?
  
👉 **Veux-tu que je continue pour te le rendre encore plus "production ready" ?** 🎯🚀  
*(ça ne prend que 2 minutes de plus !)*


