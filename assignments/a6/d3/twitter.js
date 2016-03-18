var width = 2000,
    height = 1500;

var color = d3.scale.category20();

var force = d3.layout.force()
    .charge(-350)
    .linkDistance(500)
    .size([width, height]);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.tsv("net.tsv", function(error, graph) {
  if (error) throw error;

var nodes ={}
var links=[]
graph.forEach(
  function(link){
    link.source_name = nodes[link.source_name] || 
        (nodes[link.source_name] = {name: link.source_name,});
    link.target_name = nodes[link.target_name] || 
        (nodes[link.target_name] = {name: link.target_name});

        switch(link.link_type)
        {
          case '0':
          links.push({source: link.source_name, target: link.target_name });
          break;
          case '1':
          links.push({source: link.target_name , target: link.source_name});
          break;
          case '2':
          links.push({source: link.source_name, target: link.target_name });
          links.push({source: link.target_name , target: link.source_name});
          break;
          default:
          break;
        }
  }
);

  force
      .nodes(d3.values(nodes))
      .links(links)
      .start();

// build the arrow.
svg.append("svg:defs").selectAll("marker")
    .data(["end"])
  .enter().append("svg:marker")
    .attr("id", String)
    .attr("viewBox", "0 -5 10 10")
    .attr("refX", 15)
    .attr("refY", -1.5)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
  .append("svg:path")
    .attr("d", "M0,-5L10,0L0,5");

// add the links and the arrows
var path = svg.append("svg:g").selectAll("path")
    .data(force.links())
  .enter().append("svg:path")
    .attr("class", "link")
    .attr("marker-end", "url(#end)");

  var node = svg.selectAll(".node")
      .data(force.nodes())
    .enter().append("g")
      .attr("class", "node")
      .call(force.drag);
  // add the nodes
node.append("circle")
    .attr("r", 5);

  node.append("text")
    .attr("x", 12)
    .attr("dy", ".35em")
    .text(function(d) { return d.name; });

  force.on("tick", function() {
    path.attr("d", function(d) {
        var dx = d.target.x - d.source.x,
            dy = d.target.y - d.source.y,
            dr = Math.sqrt(dx * dx + dy * dy);
        return "M" + 
            d.source.x + "," + 
            d.source.y + "A" + 
            dr + "," + dr + " 0 0,1 " + 
            d.target.x + "," + 
            d.target.y; });

    node
        .attr("transform", function(d) { 
            return "translate(" + d.x + "," + d.y + ")"; });
  });
});