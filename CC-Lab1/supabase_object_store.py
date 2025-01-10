from supabase import create_client, Client

SUPABASE_URL = "https://skbjcfbjjkcqlzylrlii.supabase.co"  # Your Supabase URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNrYmpjZmJqamtjcWx6eWxybGlpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzY1MDIwMjYsImV4cCI6MjA1MjA3ODAyNn0.yRnBRZmfdoB_D64vxT3Cfkpn488rEPAOdU0g9vwBZ-0"  # Replace with your actual Supabase API key

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Step 1: Create a storage bucket
bucket_name = "my_bucket"  # Replace with your preferred bucket name
try:
    response = supabase.storage.create_bucket(
        bucket_name,   
        options={
            "public": True,  # Make the bucket public
            "allowed_mime_types": ["image/png"],  # Allow only PNG images
            "file_size_limit": 1024 * 1024,  # Limit file size to 1MB
        }
    )
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"Bucket creation error: {e}")

# Step 2: Upload an image to the bucket
image_path = r"D:\PESU classroom\SEM 6\CC\CC-Lab1\cat.jpeg"
image_name = "cat.jpeg"

try:
    with open(image_path, 'rb') as f:
        response = supabase.storage.from_(bucket_name).upload(
            file=f,
            path=image_name,
            file_options={"content-type": "image/png", "cache-control": "3600", "upsert": False},
        )
        print(f"Image uploaded successfully: {response}")
except Exception as e:
    print(f"Image upload error: {e}")

# Step 3: Get the public URL of the image
try:
    public_url = supabase.storage.from_(bucket_name).get_public_url(image_name)
    print(f"Public URL of the image: {public_url}")
except Exception as e:
    print(f"Error getting public URL: {e}")
