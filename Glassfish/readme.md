# GlassFish

> Install Glassfish server and change HTTP port to 8088.

To install glassfish server, we have to download the zip file and unzip it.

```
wget https://download.eclipse.org/ee4j/glassfish/glassfish-6.2.2.zip 
unzip glassfish-6.2.2.zip
```

Now to change the HTTP port we need to change it from the configuration file of the domain located where the file extracted above is, i.e., **glassfish6/glassfish/domains/domain1/config**, inside the **domain.xml** file. We will change the port in the xml.

```
<network-listeners>
<network-listener port="8088" protocol="http-listener-1" transport="tcp" name="http-listener-1" thread-pool="http-thread-pool"></network-listener>
</network-listeners>
```

To start the glassfish server, we need to add glassfish as a service. So, we will create a service file **/etc/systemd/system/glassfish.service**. This file should contain the settings as such:

```
[Unit]
Description = GlassFish Server v6.2
After = syslog.target network.target

[Service]
ExecStart=/opt/glassfish6/bin/asadmin start-domain
ExecReload=/opt/glassfish6/bin/asadmin restart-domain
ExecStop=/opt/glassfish6/bin/asadmin stop-domain
Type = forking

[Install]
WantedBy = multi-user.target
```

Now to enable and start the server we run the code

```
sudo systemctl daemon-reload
sudo systemctl enable glassfish
sudo systemctl start glassfish
```

![Glassfish](screenshots/Screenshot%202021-11-15%20014526.png)

---

>Create a demo Java (11) servlet application with maven.

To install Java 11 JDK we run the command 

```
sudo apt install java-11-jdk
```

![Java](screenshots/Screenshot%202021-11-15%20010603.png))
 
So, we create a java servlet application using maven, to install maven:

```
sudo apt install maven
```

We create a new Java application using maven archetype using the command

```
mvn archetype:generate -DgroupId=com.demoproject -DartifactId=DemoProject -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false
```

![Maven](screenshots/Screenshot%202021-11-15%20022504.png)

---

>Generate war package.

To deploy our Java Servlet application, we need to create war package of the application which can be created using maven. 
Firstly, maven needs to set up to package the application as war, this can be done by updating **pom.xml** file of the project and adding line below inside the ```<project>``` tag:
```
<packaging>war</packaging>
```
Now to create the war package we need to build / package the application using the command:

```
mvn package
```

![Package](screenshots/Screenshot%202021-11-15%20022338.png)

---

>Deploy the war using glassfish app server.

To deploy the app to glassfish server, we can use asadmin utility.

```
deploy –-host localhost <path-to-war-file> 
```
![Deploy](screenshots/Screenshot%202021-11-15%20022253.png)
![Application](screenshots/Screenshot%202021-11-15%20104520.png)
