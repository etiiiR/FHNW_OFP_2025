package com.giniality.education.webappframework.registry;

import java.util.HashMap;
import java.util.Map;

import com.giniality.education.webappframework.service.Service;

/**
 * Registry to store instances of the <code>Service</code> 
 * class with their alias name.
 * 
 * @author Christian Sauer (CSA), Giniality AG
 */
public class ServiceRegistry {

	/**
	 * The registered services are here.
	 */
	private Map mappings;

	/**
	 * The alias names are here.
	 */
	private Map aliasNames;
	
	/**
	 * Static instance of this registry -> Singleton.
	 */
	private static ServiceRegistry _instance = new ServiceRegistry();

	/**
	 * Constructor not visible. Use <code>getInstance</code> 
	 * method to receive an instance of this registry.
	 */
	private ServiceRegistry() {
		mappings = new HashMap();
		aliasNames = new HashMap();
	}

	/**
	 * Gets the instance of this registry.
	 * 
	 * @return The instance.
	 */
	public static ServiceRegistry getInstance() {
		return _instance;
	}

	/**
	 * Registers the given service using the given alias name.
	 * 
	 * @param inServiceObject The service object.
	 */
	public void registerService(Service inServiceObject) {
		mappings.put(inServiceObject.getAliasName(), inServiceObject);
		aliasNames.put(inServiceObject.getClass(), inServiceObject.getAliasName());
	}

	/**
	 * Finds the service belonging to the given alias name.
	 * 
	 * @param inAliasName The alias name.
	 * 
	 * @return The service, or <code>null</code>, if the alias does not exist.
	 */
	public Service findService(String inAliasName) {
		return (Service) mappings.get(inAliasName);
	}
	
	/**
	 * Gets the alias name of the given <code>Service</code> class.
	 * @param inServiceClass the service class
	 * @return The alias name.
	 */
	public String getAliasNameForClass(Class inServiceClass) {
		return (String) aliasNames.get(inServiceClass);
	}
}