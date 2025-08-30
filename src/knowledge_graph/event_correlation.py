import networkx as nx

class EventCorrelationEngine:
    def __init__(self, bonds_df):
        self.graph = nx.Graph()
        self._build_graph(bonds_df)

    def _build_graph(self, df):
        # Add nodes for bonds, sectors, issuers
        for _, row in df.iterrows():
            bond = row['bond']
            sector = row['sector']
            issuer = row.get('issuer', None)
            self.graph.add_node(bond, type='bond')
            self.graph.add_node(sector, type='sector')
            self.graph.add_edge(bond, sector)
            if issuer:
                self.graph.add_node(issuer, type='issuer')
                self.graph.add_edge(bond, issuer)

    def propagate_event(self, affected_sector):
        # Find all bonds in the affected sector
        affected_bonds = [n for n, attr in self.graph.nodes(data=True)
                          if attr.get('type') == 'bond' and self.graph.has_edge(n, affected_sector)]
        return affected_bonds

    def get_connected(self, node):
        return list(self.graph.neighbors(node))

    def contagion_paths(self, start_node, risk_level='high'):
        # Example: return paths with color coding based on risk
        paths = []
        for neighbor in self.graph.neighbors(start_node):
            color = 'red' if risk_level == 'high' else 'green'
            paths.append({'from': start_node, 'to': neighbor, 'color': color})
        return paths

# Example usage:
# engine = EventCorrelationEngine(bonds_df)
# affected = engine.propagate_event('Tech')