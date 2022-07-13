import sys
import os
import opentumflex

def main():
    counter = 1
    while counter < 3:

        base_dir = os.path.abspath(os.getcwd())
        input_file = r'\input\input_data.xlsx'
        output_dir = r'\output\{}'.format(counter)

        path_input_data = base_dir + input_file
        path_results = base_dir + output_dir

        ems = opentumflex.run_scenario(path_results, opentumflex.scenario_mini_apartment,     # Select scenario from scenario.py
                                       path_input=path_input_data,              # Input path
                                       path_results=path_results,               # Output path
                                       solver='gurobi',                           # Select solver
                                       time_limit=50,                           # Time limit to solve the optimization
                                       save_opt_res=True,                      # Save optimization results
                                       show_opt_balance=False,                   # Plot energy balance
                                       show_opt_soc=False,                      # Plot optimized SOC plan
                                       show_flex_res=False,                     # Show flexibility plots
                                       show_aggregated_flex=False,               # Plot aggregated flex
                                       show_aggregated_flex_price=False,        # Plot aggregated price as bar/scatter
                                       save_flex_offers=True,                  # Save flexibility offers in comax/alf format
                                       convert_input_tocsv=True,                # Save .xlsx file to .csv format
                                       troubleshooting=False)                   # Troubleshooting on/off

        counter += 1
main()