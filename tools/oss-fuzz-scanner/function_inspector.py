# Copyright 2023 Fuzz Introspector Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module for reporting details about a function in a project."""

import scanner


def print_function_details(project_name, functions_to_analyse):
    report_generator = scanner.get_all_reports([project_name], 2)

    project, date_as_str, introspector_project = next(report_generator)
    all_functions = introspector_project.proj_profile.get_all_functions()

    for function_name in functions_to_analyse:
        if function_name not in all_functions:
            print(f"Could not find {function_name} in the project")
            continue

        function_profile = all_functions[function_name]
        reached_by_fuzzer_count = len(function_profile.reached_by_fuzzers)
        code_coverage = introspector_project.proj_profile.get_func_hit_percentage(
            function_name)

        print("%s" % (function_name))
        print("  Reached by %d fuzzers [%s]" %
              (reached_by_fuzzer_count, str(
                  function_profile.reached_by_fuzzers)))
        print("  Code coverage: %f" % (code_coverage))


if __name__ == "__main__":
    print_function_details('htslib', ['zlib_mem_inflate', 'vcf_write'])
