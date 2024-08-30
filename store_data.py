import psycopg2
from psycopg2 import Error
from fetch_data import DATABASE_CONNECTION_STRING
import json

def store_enriched_data(enriched_data):
    try:
        conn = psycopg2.connect(DATABASE_CONNECTION_STRING)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS enriched_company_data (
            company_id INT PRIMARY KEY,
            company_name TEXT,
            call_to_action JSONB,
            specialities TEXT[],
            employee_count_range JSONB,
            tagline TEXT,
            follower_count INT,
            original_cover_image TEXT,
            logo_resolution_result TEXT,
            industry TEXT,
            description TEXT,
            website_url TEXT,
            headquarter JSONB,
            founded_on JSONB,
            universal_name TEXT,
            url TEXT
        )
        """)

        for item in enriched_data:
            cursor.execute("""
            INSERT INTO enriched_company_data (
                company_id, company_name, call_to_action, specialities, employee_count_range, tagline, follower_count, 
                original_cover_image, logo_resolution_result, industry, description, website_url, headquarter, founded_on, 
                universal_name, url
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (company_id) DO UPDATE
            SET company_name = EXCLUDED.company_name,
                call_to_action = EXCLUDED.call_to_action,
                specialities = EXCLUDED.specialities,
                employee_count_range = EXCLUDED.employee_count_range,
                tagline = EXCLUDED.tagline,
                follower_count = EXCLUDED.follower_count,
                original_cover_image = EXCLUDED.original_cover_image,
                logo_resolution_result = EXCLUDED.logo_resolution_result,
                industry = EXCLUDED.industry,
                description = EXCLUDED.description,
                website_url = EXCLUDED.website_url,
                headquarter = EXCLUDED.headquarter,
                founded_on = EXCLUDED.founded_on,
                universal_name = EXCLUDED.universal_name,
                url = EXCLUDED.url
            """, (
                item.get('company_id'),
                item.get('company_name'),
                json.dumps(item.get('call_to_action')),
                item.get('specialities'), 
                json.dumps(item.get('employee_count_range')), 
                item.get('tagline'),
                item.get('follower_count'),
                item.get('original_cover_image'),
                item.get('logo_resolution_result'),
                item.get('industry'),
                item.get('description'),
                item.get('website_url'),
                json.dumps(item.get('headquarter')),
                json.dumps(item.get('founded_on')),
                item.get('universal_name'),
                item.get('url')
            ))

        conn.commit()
    except psycopg2.DatabaseError as e:
        conn.rollback()
        raise Exception(f"Failed to store enriched data: {e}")
    finally:
        if conn is not None:
            conn.close()
