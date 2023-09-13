import importlib.util
import timeit


if __name__ == "__main__":
    problem = "problem" + input(f"Which Problem do you want to load?\n")
    module_file_path = "./solutions/" + problem + ".py"
    spec = importlib.util.spec_from_file_location(problem, module_file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    iterations = 1000
    execution_time = timeit.timeit(module.solution, number=iterations)

    average_time_per_iteration = execution_time / iterations

    print(f"The solution of {problem} is: {module.solution()}")
    print(f"The average execution time per iteration is: {average_time_per_iteration:.6f} seconds")
