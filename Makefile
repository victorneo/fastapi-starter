all:
	uvicorn app:app --reload

test:
	DATABASE_URL=sqlite+aiosqlite:///testdb.sqlite alembic upgrade head
	pytest tests/ --envfile .test.env
	rm testdb.sqlite