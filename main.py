import multiprocessing

def calculate_sum(sub_list):
    return sum(sub_list)

if __name__ == '__main__':
    # Create a large list of numbers
    numbers = list(range(99999999))

    # Determine the number of CPU cores available for parallel processing
    num_processes = multiprocessing.cpu_count()

    # Print the number of CPU cores available
    print(f"Number of processes: {num_processes}")

    # Determine the size of each chunk of data to be processed by each CPU core
    chunk_size = len(numbers) // num_processes

    # Print the size of each chunk of data
    print(f"Chunk size: {chunk_size}")

    # Divide the list of data into sub-lists, with each sub-list containing a chunk of data
    chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]

    # Print the number of sub-lists (i.e., the number of chunks of data)
    print(f"Number of chunks: {len(chunks)}")

    # Calculate the sum of each sub-list in parallel
    with multiprocessing.Pool(processes=num_processes) as pool:
        partial_sums = pool.map(calculate_sum, chunks)

    # Combine the partial sums to obtain the final sum
    total_sum = sum(partial_sums)
    
    # Print the sum
    print(f"Total sum: {total_sum}")