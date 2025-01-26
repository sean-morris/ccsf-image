# Store in ~/.jupyter/ for user nbconvert configuration
# Store in /srv/conda/envs/notebook/etc/jupyter for system-wide nbconvert configuration

c = get_config()

# Enable embedding images in exported HTML files
c.HTMLExporter.embed_images = True
