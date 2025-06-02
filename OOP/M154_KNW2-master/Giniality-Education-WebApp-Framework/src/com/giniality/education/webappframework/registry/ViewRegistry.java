package com.giniality.education.webappframework.registry;

import java.util.HashMap;
import java.util.Map;

import com.giniality.education.webappframework.view.View;

/**
 * Registry to store instances of the <code>View</code>
 * class with their alias name.
 * 
 * @author Christian Sauer (CSA), Giniality AG
 */
public class ViewRegistry {

	/**
	 * The registered views are here.
	 */
	private Map mappings;

	/**
	 * The alias names are here.
	 */
	private Map aliasNames;
	
	/**
	 * Static instance of this registry -> Singleton.
	 */
	private static ViewRegistry _instance = new ViewRegistry();

	/**
	 * Constructor not visible. Use <code>getInstance</code> 
	 * method to receive an instance of this registry.
	 */
	private ViewRegistry() {
		mappings = new HashMap();
		aliasNames = new HashMap();
	}

	/**
	 * Gets the instance of this registry.
	 * 
	 * @return The instance.
	 */
	public static ViewRegistry getInstance() {
		return _instance;
	}

	/**
	 * Registers the given view using its alias name.
	 * 
	 * @param inViewObject The view object.
	 */
	public void registerView(View inViewObject) {
		mappings.put(inViewObject.getAliasName(), inViewObject);
		aliasNames.put(inViewObject.getClass(), inViewObject.getAliasName());
	}

	/**
	 * Finds the view belonging to the given alias name.
	 * 
	 * @param inAliasName The alias name.
	 * 
	 * @return The view object, or <code>null</code>, if the alias does not exist.
	 */
	public View findView(String inAliasName) {
		return (View) mappings.get(inAliasName);
	}
	
	/**
	 * Gets the alias name of the given <code>View</code> class.
	 * 
	 * @return The alias name.
	 */
	public String getAliasNameForClass(Class inViewClass) {
		return (String) aliasNames.get(inViewClass);
	}
}