from sqlalchemy import create_engine, text


engine = create_engine("postgresql+psycopg2://postgres.shqvhviglspulcejfrmv:Teddydaniels1886!@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres?sslmode=require", echo=True, connect_args={"connect_timeout": 10})


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from job_postings"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._asdict()))
        print(jobs)
        return jobs
       
        
