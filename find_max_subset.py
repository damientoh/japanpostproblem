def find_max_subset(max_load=30000, items=[]):
    if len(items) == 0:
        return []
        
    best_subset = []
    for index, item in enumerate(items):
        updated_items = list(items)
        updated_items.pop(index)
        if item <= max_load:
            best_subset.append([item] + find_max_subset(max_load - item, updated_items))
        else:
            best_subset.append(find_max_subset(max_load, updated_items))
    return max(best_subset, key=sum)
