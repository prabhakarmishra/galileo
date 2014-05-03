function Gauge(placeholderName, configuration)
{
	this.placeholderName = placeholderName;
	
	var self = this; // for internal d3 functions
	
	this.configure = function(configuration)
	{
		this.config = configuration;
		
		this.config.size = this.config.size * 0.9;
		
		this.config.raduis = this.config.size * 0.9 / 2;
		this.config.cx = this.config.size / 2;
		this.config.cy = this.config.size / 2;
		
		this.config.min = undefined != configuration.min ? configuration.min : 0; 
		this.config.max = undefined != configuration.max ? configuration.max : 100; 
		this.config.range = this.config.max - this.config.min;
		
		this.config.majorTicks = configuration.majorTicks || 10;
		this.config.minorTicks = configuration.minorTicks || 2;
		
		this.config.greenColor 	= configuration.greenColor || "#109618";
		this.config.yellowColor = configuration.yellowColor || "#FF9900";
		this.config.redColor 	= configuration.redColor || "#DC3912";

		this.config.bordercol 	= configuration.bordercol || "#ccc";
		
		this.config.transitionDuration = configuration.transitionDuration || 500;
	}

	this.render = function()
	{
		this.body = d3.select("#" + this.placeholderName)
							.style("position", 'relative')
							.append("svg:svg")
							.attr("class", "gauge")
							.attr("width", this.config.size)
							.attr("height", this.config.size);


		
		this.body.append("svg:circle")
					.attr("cx", this.config.cx)
					.attr("cy", this.config.cy)
					.attr("r", this.config.raduis)
					.style("fill", this.config.bordercol);

		this.body.append("svg:circle")
					.attr("cx", this.config.cx)
					.attr("cy", this.config.cy)
					.attr("r", 0.9 * this.config.raduis)
					.style("fill", "#262626");

		this.body.append("svg:circle")
					.attr("cx", this.config.cx)
					.attr("cy", this.config.cy)
					.attr("r", 0.85 * this.config.raduis)
					.style("fill", "#757571")
					.style("stroke", "#fde262")
					.style("stroke-width", "3px");
					
		var fontSize = Math.round(this.config.size / 19);
		d3.select("#" + this.placeholderName).append("span")
					.text( this.config.label )
					.style("color", "#fff")
					.style("position", "absolute")
					.style("bottom", "50px")
					.style("left", "0")
					.style("right", "0")
					.style("font-size", fontSize/1.5 + "px")
					.style("line-height", (fontSize/1.5)+1 + "px")
					.style("margin", "auto")
					.style("min-height", "35px")
					.style("width", (this.config.raduis - 34) +"px")
					.style("text-align", "center");
					
		for (var index in this.config.greenZones)
		{
			this.drawBand(this.config.greenZones[index].from, this.config.greenZones[index].to, self.config.greenColor, this.placeholderName);
		}
		
		for (var index in this.config.yellowZones)
		{
			this.drawBand(this.config.yellowZones[index].from, this.config.yellowZones[index].to, self.config.yellowColor);
		}
		
		for (var index in this.config.redZones)
		{
			this.drawBand(this.config.redZones[index].from, this.config.redZones[index].to, this.config.bordercol, this.placeholderName);
		}
		
		/*if (undefined != this.config.label)
		{
			var fontSize = Math.round(this.config.size / 19);
			this.body.append("svg:text")
						.attr("x", this.config.cx)
						.attr("y", this.config.size - this.config.cy / 2 - fontSize)
//						.attr("y", this.config.cy / 2 + fontSize / 2)
						.attr("dy", fontSize / 2)
						.attr("text-anchor", "middle")
						.text(this.config.label)
						.style("font-size", fontSize/1.5 + "px")
						.style("fill", "#fff")
						.style("stroke-width", "0px");
		}*/
		

			var fontSize = Math.round(this.config.size / 19);
			this.body.append("svg:text")
						.attr("x", this.config.cx)
						.attr("y", this.config.size - this.config.cy / 1.6 - fontSize)
						.attr("dy", fontSize / 2)
						.attr("text-anchor", "middle")
						.text('%')
						.style("font-size", fontSize/1.5 + "px")
						.style("fill", "#e37a31")
						.style("stroke-width", "0px");


		var fontSize = Math.round(this.config.size / 16);
		var majorDelta = this.config.range / (this.config.majorTicks - 1);
		for (var major = this.config.min; major <= this.config.max; major += majorDelta)
		{
			var minorDelta = majorDelta / this.config.minorTicks;
			for (var minor = major + minorDelta; minor < Math.min(major + majorDelta, this.config.max); minor += minorDelta)
			{
				var point1 = this.valueToPoint(minor, 0.55);
				var point2 = this.valueToPoint(minor, 0.63);
				
				this.body.append("svg:line")
							.attr("x1", point1.x)
							.attr("y1", point1.y)
							.attr("x2", point2.x)
							.attr("y2", point2.y)
							.style("stroke", "#fff")
							.style("stroke-width", "1px");
			}
			
			var point1 = this.valueToPoint(major, 0.5);
			var point2 = this.valueToPoint(major, 0.65);	
			
			this.body.append("svg:line")
						.attr("x1", point1.x)
						.attr("y1", point1.y)
						.attr("x2", point2.x)
						.attr("y2", point2.y)
						.style("stroke", "#fff")
						.style("stroke-width", "1px");
			
			//if (major == this.config.min || major == this.config.max)
			//{
				var point = this.valueToPoint(major, 0.75);
				
				this.body.append("svg:text")
				 			.attr("x", point.x)
				 			.attr("y", point.y)
				 			.attr("dy", fontSize / 4)
				 			.attr("text-anchor", major < 45 ? "middle" : "middle")
				 			.text(major)
				 			.style("font-size", (fontSize/1.4) + "px")
							.style("fill", "#fff")
							.style("stroke-width", "0px");
			//}
		}
		
		var pointerContainer = this.body.append("svg:g").attr("class", "pointerContainer");
		
		var midValue = (this.config.min + this.config.max) / 2;
		
		var pointerPath = this.buildPointerPath(midValue);
		
		var pointerLine = d3.svg.line()
									.x(function(d) { return (d.x/2) })
									.y(function(d) { return (d.y/1.4) })
									.interpolate("basis");
		
		pointerContainer.selectAll("path")
							.data([pointerPath])
							.enter()
								.append("svg:path")
									.attr("d", pointerLine)
									.style("fill", "#dc3912")
									.style("stroke", "#c63310")
									.style("fill-opacity", 0.7)
					
		 var newid = this.placeholderName+'radial'; 
		var defs = pointerContainer.append('svg:defs');
		defs.append('svg:radialGradient')
		.attr('cx', '50%').attr('cy', '0%').attr('fx', '50%').attr('r', '80%').attr('fy', '50%')
		.attr('id', newid).call(
		function(gradient) {
		gradient.append('svg:stop').attr('offset', '0%').attr('style', 'stop-color:rgb(220,203,174);stop-opacity:0.8');
		gradient.append('svg:stop').attr('offset', '100%').attr('style', 'stop-color:rgb(224, 135, 70);stop-opacity:1');
		});

		pointerContainer.append("svg:circle")
							.style("fill", 'url(#' + newid +')')
							.attr("cx", this.config.cx)
							.attr("cy", this.config.cy)
							.attr("r", 0.16 * this.config.raduis)
							.style("opacity", 1);
		
		var fontSize = Math.round(this.config.size / 10);
		/*pointerContainer.selectAll("text")
							.data([midValue])
							.enter()
								.append("svg:text")
									.attr("x", this.config.cx)
									.attr("y", this.config.size - this.config.cy / 4 - fontSize)
									.attr("dy", fontSize / 2)
									.attr("text-anchor", "middle")
									.style("font-size", fontSize + "px")
									.style("fill", "#000")
									.style("stroke-width", "0px");
		*/
		this.redraw(this.config.min, 0);
	}
	
	this.buildPointerPath = function(value)
	{
		var delta = this.config.range / 13;
		
		var head = valueToPoint(value, 0.85);
		var head1 = valueToPoint(value - delta, 0.12);
		var head2 = valueToPoint(value + delta, 0.12);
		
		var tailValue = value - (this.config.range * (1/(270/360)) / 2);
		var tail = valueToPoint(tailValue, 0.28);
		var tail1 = valueToPoint(tailValue - delta, 0.12);
		var tail2 = valueToPoint(tailValue + delta, 0.12);
		
		return [head, head1, tail2, tail, tail1, head2, head];
		
		function valueToPoint(value, factor)
		{
			var point = self.valueToPoint(value, factor);
			point.x -= self.config.cx;
			point.y -= self.config.cy;
			return point;
		}
	}
	
	this.drawBand = function(start, end, color, placeholderName)
	{
		if (0 >= end - start) return;
		
		var defs = this.body.append('svg:defs');
		 var newid = placeholderName+'master'; 
		defs.append('svg:linearGradient')
		.attr('x1', '0%').attr('y1', '0%').attr('x2', '0%').attr('y2', '100%')
		.attr('id', newid).call(
		function(gradient) {
		gradient.append('svg:stop').attr('offset', '0%').attr('style', 'stop-color:rgb(245,227,100);stop-opacity:1');
		gradient.append('svg:stop').attr('offset', '100%').attr('style', 'stop-color:'+color+';stop-opacity:1');
		});

		this.body.append("svg:path")
					.style("fill", 'url(#' + newid +')')
					.attr("d", d3.svg.arc()
						.startAngle(this.valueToRadians(start))
						.endAngle(this.valueToRadians(end))
						.innerRadius(0.55 * this.config.raduis)
						.outerRadius(0.68 * this.config.raduis))
					.attr("transform", function() { return "translate(" + self.config.cx + ", " + self.config.cy + ") rotate(270)" });
	}
	
	this.redraw = function(value, transitionDuration)
	{
		var pointerContainer = this.body.select(".pointerContainer");
		
		pointerContainer.selectAll("text").text(Math.round(value));
		
		var pointer = pointerContainer.selectAll("path");
		pointer.transition()
					.duration(undefined != transitionDuration ? transitionDuration : this.config.transitionDuration)
					//.delay(0)
					//.ease("linear")
					//.attr("transform", function(d) 
					.attrTween("transform", function()
					{
						var pointerValue = value;
						if (value > self.config.max) pointerValue = self.config.max + 0.02*self.config.range;
						else if (value < self.config.min) pointerValue = self.config.min - 0.02*self.config.range;
						var targetRotation = (self.valueToDegrees(pointerValue) - 90);
						var currentRotation = self._currentRotation || targetRotation;
						self._currentRotation = targetRotation;
						
						return function(step) 
						{
							var rotation = currentRotation + (targetRotation-currentRotation)*step;
							return "translate(" + self.config.cx + ", " + self.config.cy + ") rotate(" + rotation + ")"; 
						}
					});
	}
	
	this.valueToDegrees = function(value)
	{
		// thanks @closealert
		//return value / this.config.range * 270 - 45;
		return value / this.config.range * 270 - (this.config.min / this.config.range * 270 + 45);
	}
	
	this.valueToRadians = function(value)
	{
		return this.valueToDegrees(value) * Math.PI / 180;
	}
	
	this.valueToPoint = function(value, factor)
	{
		return { 	x: this.config.cx - this.config.raduis * factor * Math.cos(this.valueToRadians(value)),
					y: this.config.cy - this.config.raduis * factor * Math.sin(this.valueToRadians(value)) 		};
	}
	
	// initialization
	this.configure(configuration);	
}



function projectpie(placeholderName, configuration)
{
	this.placeholderName = placeholderName;
	
	var self = this; // for internal d3 functions
	
	this.configure = function(configuration)
	{
		this.config = configuration;
		
		this.config.size = this.config.size * 0.9;
		
		this.config.raduis = this.config.size * 0.9 / 2;
		this.config.cx = this.config.size / 2;
		this.config.cy = this.config.size / 2;
		
		this.config.min = undefined != configuration.min ? configuration.min : 0; 
		this.config.max = undefined != configuration.max ? configuration.max : 100; 
		this.config.range = this.config.max - this.config.min;
				
		this.config.col1 	= configuration.col1 || "#109618";
		this.config.col2 = configuration.col2 || "#FF9900";
	}

	this.render = function()
	{

		this.body = d3.select("#" + this.placeholderName)
							.append("svg:svg")
							.attr("class", "projectpie")
							.attr("width", this.config.size)
							.attr("height", this.config.size);
		
			this.drawBand(this.config.min, this.config.max, this.config.col1, this.config.col2, this.placeholderName);

			var fontSize = Math.round(this.config.size / 8);
			this.body.append("svg:text")
						.attr("x", this.config.cx)
						.attr("y", this.config.size / 2.4)
//						.attr("y", this.config.cy / 2 + fontSize / 2)
						.attr("dy", fontSize )
						.attr("text-anchor", "middle")
						.text(this.config.max+"%")
						.style("font-size", fontSize + "px")
						.style("fill", "#666")
						.style("stroke-width", "0px");


	}
	

	this.drawBand = function(start, end, color1, color2, placeholderName)
	{
		if (0 >= end - start) return;

		this.body.append("svg:path")
					.style("fill", color2)
					.attr("d", d3.svg.arc()
//						.startAngle(45 * (Math.PI/180))
						.startAngle(this.valueToRadians(0))
						.endAngle(this.valueToRadians(100))
						.innerRadius(0.40 * this.config.raduis)
						.outerRadius(0.68 * this.config.raduis))
						.attr("transform", function() { return "translate(" + self.config.cx + ", " + self.config.cy + ") rotate(0)" });

		this.body.append("svg:path")
					.style("fill", color1)
					.attr("d", d3.svg.arc()
//						.startAngle(45 * (Math.PI/180))
						.startAngle(this.valueToRadians(0))
						.endAngle(this.valueToRadians(end))
						.innerRadius(0.40 * this.config.raduis)
						.outerRadius(0.68 * this.config.raduis))
						.attr("transform", function() { return "translate(" + self.config.cx + ", " + self.config.cy + ") rotate(0)" });
	}

	this.valueToDegrees = function(value)
	{
		// thanks @closealert
		return value / this.config.range * 200 ;
		//return value / this.config.range * 270 - (this.config.min / this.config.range * 270 + 45);
	}
	
	this.valueToRadians = function(value)
	{
		return ((value/100)*360) * Math.PI / 180;
	}
	
	this.valueToPoint = function(value, factor)
	{
		return { 	x: this.config.cx - this.config.raduis * factor * Math.cos(this.valueToRadians(value)),
					y: this.config.cy - this.config.raduis * factor * Math.sin(this.valueToRadians(value)) 		};
	}

	// initialization
	this.configure(configuration);	
}