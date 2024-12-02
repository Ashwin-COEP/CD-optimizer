# core.py

from prompt import extract_details, create_prow_job

prompt_text = input("Enter a prompt containing name-of-script, frequency, e.g. every day and the CPU time in ms. Leave blank to see an example: ")
if prompt_text == "":
    # Example prompt to test the function
    prompt_text = "I want to run unit-tests.sh every day using 4000ms CPU"
params = extract_details(prompt_text)
params["base_ref"] = "master"
params["org"] = "Ashwin-COEP"
params["repo"] = "CD-optimizer"
print(f"Script Name: {params["script_name"]}")
print(f"CPU Capacity: {params["cpu"]}")
print(f"Frequency (crontab format): {params["crontab_frequency"]}")
prow_job_yaml = create_prow_job(params)

# Save YAML to a file
with open("prowjob.yaml", "w") as file:
    file.write(prow_job_yaml)
