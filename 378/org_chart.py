class EmployeeNode:
    def __init__(self, value=None, left=None, right=None):
        """Initialize an EmployeeNode.

        Args:
            value (str): The role (or name) of the employee.
            left (EmployeeNode, optional): Pointer to the left child (i.e. direct report). Defaults to None.
            right (EmployeeNode, optional): Pointer to the right child (i.e. direct report). Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right


def build_org_chart(org_list: list) -> EmployeeNode:
    """
    Builds an organizational chart (binary tree representation) from a list representation of the org chart.
    The input is given as a list of employee roles or "None" values.
    A "None" value represents an absence of a node (i.e. no employee in that position).

    Example:
        org_list = ["CEO", "CFO", None, "COO", None, None, "CTO"]
        This represents:
               CEO
              /   \
            CFO   COO
                 /   \
               CTO

    Args:
        org_list (list): The list representation of the organization.

    Returns:
        EmployeeNode: The root node of the constructed organizational tree.
    """

    if not org_list:
        return None

    # Create the root node with the first value from the list
    root = EmployeeNode(org_list.pop(0))
    node_queue = [root]

    # Iterate until we've processed all node values or until there are no nodes left in the queue
    while node_queue and org_list:
        # Take the next node from the front of the queue to process
        current_node = node_queue.pop(0)

        # Process the left child
        left_value = org_list.pop(0)
        if left_value is not None:
            current_node.left = EmployeeNode(left_value)
            node_queue.append(current_node.left)

        # Check if there are still values left to process
        if org_list:
            # Process the right child
            right_value = org_list.pop(0)
            if right_value is not None:
                current_node.right = EmployeeNode(right_value)
                node_queue.append(current_node.right)
    return root


def find_depth(node: EmployeeNode | None, depth_above: int = 0) -> int:
    if node is None:
        return depth_above
    else:
        return max(
            find_depth(node.left, depth_above+1),
            find_depth(node.right, depth_above+1))


def max_depth(root: EmployeeNode) -> int:
    """Return the maximum depth (or height) of the organizational tree."""
    return find_depth(root)
