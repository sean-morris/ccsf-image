# Store in etc/jupyter/ for system-wide nbconvert configuration
# Store in ~/.jupyter/ for user nbconvert configuration

c = get_config()

# Enable embedding images in exported HTML files
c.HTMLExporter.embed_images = True
