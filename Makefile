all:
	uvicorn app:app --reload

test:
	DATABASE_URL=sqlite+aiosqlite:///testdb.sqlite alembic upgrade head
	-pytest --cov=. --cov-report term-missing tests/ --envfile .test.env
	rm testdb.sqlite
