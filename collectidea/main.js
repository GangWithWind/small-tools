define([
    'base/js/namespace',
    'jquery',
    'require',
    'base/js/events',
    'base/js/utils',
], function(Jupyter, $, require, events, configmod, utils) {
    "use strict";
	 function collect_cell(file){
		 var cell = IPython.notebook.get_selected_cell();
		 var indice = IPython.notebook.get_selected_cells_indices();
		 
       if (cell.mode == "command") {

			  var text = 'import json\n';
			  text += 'with open("'+ file +'", "r") as fid:\n'
			  text += '    pynb = json.load(fid)\n'
			  
			  
           var selected_cells = IPython.notebook.get_selected_cells();
           for (var i in selected_cells) {
               var j = selected_cells[i].toJSON();
					text += 'json_str = r"""\n'
               text += JSON.stringify(j) + "\n";
					text += '"""\n'
					text += "pynb['cells'].append(json.loads(json_str))\n"
           }
			  
			  text += 'with open("'+ file +'", "w") as fid:\n'
			  text += '    pynb = json.dump(pynb, fid)\n'
			  
           var new_cell = IPython.notebook.insert_cell_below('code');
           new_cell.set_text(text);
			  new_cell.execute();
			  
			  var new_indice = indice[indice.length-1];
	  		  indice.push(new_indice)+1;
			  IPython.notebook.delete_cells(indice);
		  }
	  }
		  
	  	  
    var load_extension = function() {
             Jupyter.toolbar.add_buttons_group([
                 {
                      'label'   : 'To knowledge',
                      'icon'    : 'fa-graduation-cap',
                      'callback': function () {
								 collect_cell("/Users/gangzhao/GELILEO/knowledge.ipynb");
							 }
								
                 },
                 {
                      'label'   : 'To Input box',
                      'icon'    : 'fa-envelope-o',
                      'callback': function () {
								 collect_cell("/Users/gangzhao/GELILEO/inputbox.ipynb");
                                                    // Jupyter.notebook.insert_cell_below('code');
                                                    // Jupyter.notebook.select_next();
                                                    // Jupyter.notebook.focus_cell();
                      }
                 }
                 ]);
             $('#insert_above_below').remove()

    };



    var extension = {
        load_jupyter_extension : load_extension,
        load_ipython_extension : load_extension
    };
    return extension;
});
