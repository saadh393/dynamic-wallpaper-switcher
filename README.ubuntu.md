# How to Run a Python Script in the Background on Ubuntu Startup

This guide will walk you through the process of setting up a Python script to run automatically in the background when your Ubuntu system starts up.

## Prerequisites

- Ubuntu operating system
- Python script you want to run (e.g., `/home/username/your_script.py`)
- sudo privileges

## Steps

1. **Create a systemd service file**

   Open a terminal and create a new service file using a text editor. Replace `username` with your actual username:

   ```bash
   sudo nano /etc/systemd/system/your-script.service
   ```

2. **Add service configuration**

   Paste the following content into the file, replacing `username` and the script path as necessary:

   ```ini
   [Unit]
   Description=Your Script Service
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /home/username/your_script.py
   WorkingDirectory=/home/username
   Restart=on-failure
   RestartSec=5
   User=username
   Group=username
   Environment=PYTHONUNBUFFERED=1
   StandardOutput=append:/var/log/your-script.log
   StandardError=append:/var/log/your-script.log

   [Install]
   WantedBy=multi-user.target
   ```

   Save and close the file (in nano: Ctrl+X, then Y, then Enter).

3. **Set correct permissions**

   ```bash
   sudo chmod 644 /etc/systemd/system/your-script.service
   ```

4. **Create log file**

   ```bash
   sudo touch /var/log/your-script.log
   sudo chown username:username /var/log/your-script.log
   ```

5. **Reload systemd**

   ```bash
   sudo systemctl daemon-reload
   ```

6. **Enable the service**

   ```bash
   sudo systemctl enable your-script.service
   ```

7. **Start the service**

   ```bash
   sudo systemctl start your-script.service
   ```

8. **Check the status**

   ```bash
   sudo systemctl status your-script.service
   ```

## Troubleshooting

If your script doesn't run correctly:

1. Check the logs:
   ```bash
   tail -f /var/log/your-script.log
   ```

2. Use journalctl for more detailed logs:
   ```bash
   journalctl -u your-script.service -f
   ```

3. Make sure all file paths in your script are absolute paths.

4. Ensure your script has the necessary permissions to run and access required files.

5. If your script modifies the desktop environment, you might need to use a different method, such as adding it to startup applications instead of a system service.

## Conclusion

Your Python script should now run in the background every time your Ubuntu system starts up. If you make changes to your script, remember to restart the service:

```bash
sudo systemctl restart your-script.service
```

For any updates to the service file itself, reload the daemon before restarting:

```bash
sudo systemctl daemon-reload
sudo systemctl restart your-script.service
```