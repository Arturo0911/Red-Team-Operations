<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** MySQL database username */
define( 'DB_USER', 'wpadmin' );

/** MySQL database password */
define( 'DB_PASSWORD', 'BestAdministrator@2020!' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'KkY%W@>T}4CKTw5{.n_j3bywoB0k^|OKX0{}5|UqZ2!VH!^uWKJ.O oROc,h pp:' );
define( 'SECURE_AUTH_KEY',  '*MHA-~<-,*^$raDR&uxP)k(~`k/{PRT(6JliOO9XnYYbFU?Xmb#9USEjmgeHYYpm' );
define( 'LOGGED_IN_KEY',    ')F6L,A23Tbr9yhrhbgjDHJPJe?sCsDzDow-$E?zYCZ3*f40LSCIb] E%zrW@bs3/' );
define( 'NONCE_KEY',        'g?vl(p${jG`JvDxVw-]#oUyd+uvFRO1tAUZQG_sGg&Q7O-*tF[KIe$weE^$bB3%C' );
define( 'AUTH_SALT',        '8>PIil3 7re_:3&@^8Zh|p^I8rwT}WpVr5|t^ih05A:]xjTA,UVXa8ny:b--/[Jk' );
define( 'SECURE_AUTH_SALT', 'dN c^]m:4O|GyOK50hQ1tumg4<JYlD2-,r,oq7GDjq4M Ri:x]Bod5L.S&.hEGfv' );
define( 'LOGGED_IN_SALT',   'tCWVbTcE*_T_}X3#t+:)>N+D%?vVAIw#!*&OK78M[@ YT0q):G~A:hTv`bO<,|68' );
define( 'NONCE_SALT',       'sa>i39)9<vVyhE3auBVzl%=p23NJbl&)*.{`<*>;R2=QHqj_a.%({D4yI-sy]D8,' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
