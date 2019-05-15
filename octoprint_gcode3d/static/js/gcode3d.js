$(function() {
	function Gcode3DViewModel(parameters) {
		var self = this;

		self.gcode = parameters[0];

		self.rendered3D = ko.observable(false);

		self.onBeforeBinding = function(){
			$('#canvas_container').before('<div id="3d_container" data-bind="visible: rendered3D"></div>');
			$('#gcode div.progress').after('<div class="row-fluid" id="gcode3d"><button type="button" class="btn btn-block" data-bind="click: toggle3D, css: { \'btn-primary\': rendered3D }">3D</button></div>')
		}

		self.toggle3D = function() {
			if(self.rendered3D()) {
				$('#canvas_container').show();
				self.rendered3D(false);
			} else {
				$('#canvas_container').hide();
				GCODE.renderer3d.setModel(GCODE.renderer.debugGetModel());
				GCODE.renderer3d.doRender();
				self.rendered3D(true);
			}
		}
	}

	OCTOPRINT_VIEWMODELS.push({
		construct: Gcode3DViewModel,
		dependencies: ["gcodeViewModel"],
		elements: ["#gcode3d","#3d_container"]
	});
});
