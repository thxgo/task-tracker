list:
	python3 task.py list $(status)

add:
	python3 task.py add "$(description)"

delete:
	python3 task.py delete $(id)

update:
	python3 task.py update $(id) "$(description)"

mark-done:
	python3 task.py mark-done $(id)

mark-in-progress:
	python3 task.py mark-in-progress $(id)
