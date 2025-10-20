from dcim.models import Site
from extras.scripts import Script, StringVar, ChoiceVar
import yaml

class FilterSitesByStatus(Script):
    """
    Custom Netbox script that filters sites by their status ("planned" or "active")
    and outputs the results in YAML format
    """

    site_status = ChoiceVar(
        description="Filter sites by status('planned' or 'active')",
        choices=(("active", "active"), ("planned", "planned")),
        required=True,
    )

    class Meta:
        name = "Filter Sites"
        description = "Iterate thorugh all sites matching the selected status and output in YAML format."

    def run(self, data, commit=True):
        """
        Execute the script.

        Args:
            data (dict): input data from Netbox UI form.
            commit (bool): whether to apply changes to the database (unused here).

        Returns:
            str: YAML string containing the filtered sites.
        """
        try:
            selected_status = data["site_status"]
            if not selected_status:
                raise ValueError("No site status provided")
            
            self.log_info(f"Filtering sites with status: {selected_status}")

            # Database query
            sites = Site.objects.filter(status=selected_status)

            if not sites.exists():
                self.log_warning(f"No sites found with status '{selected_status}'")
                return yaml.dump({"sites": []}, sort_keys=False)
                
            # Preparing Output
            output_data = []
            for site in sites:
                self.log_info(f"#{site.id}: {site.name} - {{site.status}}")
                output_data.append(
                    {"id": site.id, "name": site.name, "status": site.status}
                )

            return yaml.dump({"sites": output_data}, sort_keys=False)
              
        except Exception as e: 
            self.log_failure(f"An error ocurred: {str(e)}")
            error_output = {
                "error": str(e),
                "status": "failed"
            }
            return yaml.dump(error_output, sort_keys=False)
