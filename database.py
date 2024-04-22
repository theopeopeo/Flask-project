from sqlalchemy import create_engine, text
engine = create_engine("postgresql+psycopg2://postgres.shqvhviglspulcejfrmv:Teddydaniels1886!!@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres")

with engine.connect() as conn:
    print(conn)
    result = conn.execute(text("select * from job_postings"))
    print(result.all())