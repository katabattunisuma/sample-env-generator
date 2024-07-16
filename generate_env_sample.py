# Define a list of sensitive keys
sensitive_keys = [
    "API_KEY",
    "SECRET_KEY",
    "PASSWORD",
    "ACCESS_TOKEN",
    "DB_PASSWORD",
    "DB_USER",
    "DB_HOST",
    "DB_PORT",
    "DATABASE_URL",
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
    "SMTP_PASSWORD",
    "SMTP_USER",
    "PRIVATE_KEY",
    "CLIENT_SECRET",
    "OAUTH_TOKEN",
    "JWT_SECRET",
    "SSL_CERT",
    "SSL_KEY",
    "ENCRYPTION_KEY",
    "SESSION_SECRET",
    "PAYPAL_CLIENT_ID",
    "PAYPAL_CLIENT_SECRET",
    "STRIPE_SECRET_KEY",
    "GITHUB_TOKEN",
    "TWILIO_AUTH_TOKEN",
    "SENDGRID_API_KEY",
    "GOOGLE_CLIENT_ID",
    "GOOGLE_CLIENT_SECRET",
    "FACEBOOK_APP_ID",
    "FACEBOOK_APP_SECRET",
    "TWITTER_API_KEY",
    "TWITTER_API_SECRET",
    "REDIS_PASSWORD",
    "MONGO_URI",
    "FIREBASE_API_KEY",
    "FIREBASE_AUTH_DOMAIN",
    "FIREBASE_DATABASE_URL",
    "FIREBASE_PROJECT_ID",
    "FIREBASE_STORAGE_BUCKET",
    "FIREBASE_MESSAGING_SENDER_ID",
    "FIREBASE_APP_ID",
    # Add more as needed
]

# Read the .env file and store the lines
env_lines = []

with open("folder/.env", "r") as env_file:
    for line in env_file:
        env_lines.append(line.strip())

# Write the sample .env file
with open("folder/.env-sample", "w") as sample_env_file:
    for line in env_lines:
        # Split the line into key and value
        key_value = line.split("=", 1)
        if key_value[0] in sensitive_keys:
            # If the key is sensitive, replace the value with 'XXXXX'
            sample_env_file.write(f"{key_value[0]}=XXXXX\n")
        else:
            # Otherwise, write the line as is
            sample_env_file.write(f"{line}\n")
