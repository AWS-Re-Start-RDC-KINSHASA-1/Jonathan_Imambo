#!/bin/bash
yum update -y              # Mettre à jour les packages
yum install httpd -y       # Installer Apache HTTP Server

# Activer et démarrer le service httpd
systemctl enable httpd
systemctl start httpd

# Créer et écrire le contenu du fichier index.html
cat <<EOF > /var/www/html/index.html
<!DOCTYPE html>
<html>
<head>
    <title>echo "<html><h1>${HOSTNAME}</h1></html>" > /var/www/html/index.html</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a test page deployed using UserData script on AWS EC2 instance.</p>
</body>
</html>
EOF