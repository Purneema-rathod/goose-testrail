# Installing TestRail Extension for Goose

## Installation Steps

1. **Locate Goose Extensions Directory**
   ```bash
   # On macOS/Linux:
   cd ~/.goose/extensions/
   
   # On Windows:
   cd %USERPROFILE%\.goose\extensions\
   ```

2. **Create TestRail Extension Directory**
   ```bash
   mkdir testrail
   ```

3. **Extract Extension Files**
   ```bash
   # On macOS/Linux:
   unzip ~/testrail_extension.zip -d ~/.goose/extensions/testrail/
   
   # On Windows:
   # Use Windows Explorer to extract testrail_extension.zip to:
   # %USERPROFILE%\.goose\extensions\testrail\
   ```

4. **Configure the Extension**
   - Open Goose Desktop Application
   - Click on Settings (⋮ menu in top right)
   - Go to Extensions tab
   - Find "TestRail" in the list
   - Click "Enable"
   - Enter your TestRail credentials:
     ```yaml
     base_url: https://afterpay.testrail.io
     username: your-email@example.com
     password: your-api-key
     ```

5. **Verify Installation**
   - Open Goose chat
   - Type: `help testrail`
   - You should see the available TestRail commands

## Troubleshooting

If you encounter issues:

1. **Extension Not Found**
   - Verify the files are in the correct directory
   - Check file permissions
   - Restart Goose application

2. **Authentication Errors**
   - Verify your TestRail credentials
   - Check if you need to generate a new API key
   - Ensure you have access to the TestRail instance

3. **General Issues**
   - Check Goose logs for errors
   - Verify your internet connection
   - Make sure TestRail is accessible

## Need Help?

Contact support at purneemarathod@gmail.com with:
- Error messages
- Screenshots
- Your Goose version
- Your operating system